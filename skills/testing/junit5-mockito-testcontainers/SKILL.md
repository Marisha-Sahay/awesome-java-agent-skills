---
name: junit5-mockito-testcontainers
description: Guidelines for writing robust, modern Java tests using JUnit 5, Mockito, and Testcontainers.
---

# Testing Mastery Skill

This skill focuses on best practices for writing high-quality tests in modern Java applications.

## Testing Pattern
Enforce the AAA (Arrange, Act, Assert) or BDD (Given, When, Then) pattern in all tests to ensure tests are highly readable and structured consistently.

**Example Context:**
```java
@Test
void shouldCalculateTotalCorrectly() {
    // Arrange
    Order order = new Order(100.0, 0.1); // price, discount
    
    // Act
    double total = orderService.calculateTotal(order);
    
    // Assert
    assertThat(total).isEqualTo(90.0);
}
```

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
    void shouldProcessPayment() {
        // Arrange
        OrderRequest request = new OrderRequest("C123", new BigDecimal("100.0"));
        given(paymentClient.charge(any())).willReturn(true);

        // Act & Assert
        assertThat(orderService.process(request)).isTrue();
        verify(paymentClient).charge(any());
    }
}
```

## Integration Tests
Mandate the use of **Testcontainers** for database integration testing instead of relying on in-memory databases like H2. This ensures environment parity and prevents bugs that only occur in the production database system.

**Example Context:**
```java
@Testcontainers
@SpringBootTest
class OrderRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15-alpine");

    @DynamicPropertySource
    static void registerPgProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
    
    // tests here...
}
```

## Frameworks
Specify JUnit 5 (Jupiter) for the testing framework and Mockito 5+ for mocking.
