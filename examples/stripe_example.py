import stripe

# Stripe API test/live keys
stripe.api_key = 'YOUR_STRIPE_API_KEY'

# Create a new customer
customer = stripe.Customer.create(
    email='customer@example.com',
    name='Customer Name'
)

# Print the customer ID
print(f"Customer ID: {customer['id']}")

# Create a new charge for the customer
charge = stripe.Charge.create(
    amount=2000,  # Amount in cents
    currency='usd',
    customer=customer['id'],
    description='Sample Charge'
)

# Print the charge ID
print(f"Charge ID: {charge['id']}")
