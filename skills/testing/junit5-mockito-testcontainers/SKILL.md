---
name: junit5-mockito-testcontainers
description: Use when writing or fixing Java tests with JUnit 5, Mockito or Testcontainers, when a test mocks domain objects or value types, or when a Spring Boot integration test runs against H2 or another in-memory database instead of the production database.
---

# Testing Mastery Skill

This skill focuses on best practices for writing high-quality tests in modern Java applications.

## Testing Pattern
Enforce the AAA (Arrange, Act, Assert) or BDD (Given, When, Then) pattern in all tests to ensure tests are highly readable and structured consistently.

**Example Context:**
```java
@Test
void appliesTheDiscountToTheOrderTotal() {
    // Arrange
    Order order = new Order(new BigDecimal("100.00"), new BigDecimal("0.10")); // price, discount rate

    // Act
    BigDecimal total = orderService.calculateTotal(order);

    // Assert
    assertThat(total).isEqualByComparingTo("90.00");
}
```

Model money as `BigDecimal`, never `double`, and compare it with `isEqualByComparingTo`. `isEqualTo` also compares scale, so `90.0` and `90.00` are not equal under it.

## Test-First in Java
When writing the test before the code, a compile error is not the failing test: a test that doesn't compile never ran, so it shows nothing about whether its assertions can fail.

1. Write the test.
2. Add only the signatures it needs (constructor, method), with a body that returns a deliberately wrong value. Don't throw from the stub: Surefire reports an exception as `Errors: 1`, not as a failed assertion.
3. Run the test and confirm `Failures: 1` with the assertion message you expect, such as `Expecting value to be false but was true`.
4. Implement, then run it again and see it pass.

If a stub's default value already passes the test (a stub returning `false` passes a test that expects `false`), the test can't tell the stub from the real rule: add the opposite case before implementing.

## Mocking
Instruct the agent to avoid over-mocking. Mock external boundaries and slow dependencies, but use real domain objects. Avoid mocking simple value types or internal application logic when possible. Use Mockito 5+ for all mocking needs.

**Example Context:**
```java
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {

    @Mock
    private PaymentClient paymentClient; // External boundary

    @InjectMocks
    private OrderService orderService;

    @Test
    void chargesTheCustomerForTheOrderAmount() {
        // Arrange
        OrderRequest request = new OrderRequest("C123", new BigDecimal("100.00"));
        given(paymentClient.charge(any(Charge.class))).willReturn(true);

        // Act
        boolean processed = orderService.process(request);

        // Assert
        assertThat(processed).isTrue();
        ArgumentCaptor<Charge> charge = ArgumentCaptor.forClass(Charge.class);
        then(paymentClient).should().charge(charge.capture());
        assertThat(charge.getValue().customerId()).isEqualTo("C123");
        assertThat(charge.getValue().amount()).isEqualByComparingTo("100.00");
    }
}
```

`verify(paymentClient).charge(any())` passes whatever amount is charged. When the arguments are what the test is about, capture them and assert their values. On paths that must not reach the boundary, such as a rejected order, assert `then(paymentClient).shouldHaveNoInteractions()`.

## Mocking Spring Beans
When only one layer is under test, prefer a test slice such as `@WebMvcTest` over `@SpringBootTest`, and replace its collaborators with `@MockitoBean` (Spring Framework 6.2+, Spring Boot 3.4+). `@MockBean` is deprecated since Spring Boot 3.4 and removed in Spring Boot 4.

**Example Context:**
```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean
    private OrderService orderService;

    @Test
    void returns404WhenTheOrderDoesNotExist() throws Exception {
        given(orderService.find("O-404")).willThrow(new OrderNotFoundException("O-404"));

        mockMvc.perform(get("/api/orders/O-404"))
                .andExpect(status().isNotFound());
    }
}
```

## Asynchronous Code
Awaitility comes with `spring-boot-starter-test`. To assert on work done by `@Async` methods, event listeners or message consumers, poll with it instead of `Thread.sleep` or a hand-written loop:

```java
await().atMost(Duration.ofSeconds(5))
        .untilAsserted(() -> assertThat(auditLog.entriesFor("O-200")).hasSize(1));
```

## Integration Tests
Mandate the use of **Testcontainers** for database integration testing instead of relying on in-memory databases like H2. This ensures environment parity and prevents bugs that only occur in the production database system.

**Example Context:**
```java
@Testcontainers
@SpringBootTest
class OrderRepositoryTest {

    @Container
    @ServiceConnection
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16-alpine");

    // tests here...
}
```

`@ServiceConnection` (Spring Boot 3.1+, from the `spring-boot-testcontainers` test dependency) points the datasource at the container. It replaces a `@DynamicPropertySource` method that copies the JDBC URL, username and password; keep `@DynamicPropertySource` only for properties no service connection covers.

With Spring Boot 4 (Testcontainers 2), the module is `org.testcontainers:testcontainers-postgresql` and the class is `org.testcontainers.postgresql.PostgreSQLContainer`, which is no longer generic: declare `static PostgreSQLContainer postgres`.

## Frameworks
Use JUnit Jupiter (JUnit 5 with Spring Boot 3, JUnit 6 with Spring Boot 4), Mockito 5+ and AssertJ.
