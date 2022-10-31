import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

print(EMAIL_HOST_PASSWORD)