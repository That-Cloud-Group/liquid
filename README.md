# liquid

An SDK for security tools for automation purposes.

## Usage

`pip install liquid`

Example usage:
```
AQUA_CLIENT = liquid.client("aqua_cwp", {"auth_options": {"ssl_verify": False}})
scopes = AQUA_CLIENT.application_scopes.list_application_scopes()

for scope in scopes:
    print(f"Found application scope with name {scope['name']}")
```

## Contributing
