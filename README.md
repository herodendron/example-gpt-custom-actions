# Example GPT Custom Actions

The following repo is a text Python API for gpt custom actions that can be deployed on Vercel. Schema:

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "Sample Flask API",
    "description": "A simple Flask API for processing data",
    "version": "v1.0.0"
  },
  "servers": [
    {
      "url": "http://localhost:5000"
    }
  ],
  "paths": {
    "/": {
      "get": {
        "summary": "Home",
        "operationId": "home",
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "text/plain": {
                "example": "Hello, World hey hey!"
              }
            }
          }
        }
      }
    },
    "/about": {
      "get": {
        "summary": "About",
        "operationId": "about",
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "text/plain": {
                "example": "About"
              }
            }
          }
        }
      }
    },
    "/process_data": {
      "post": {
        "summary": "Process Data",
        "operationId": "processData",
        "requestBody": {
          "description": "JSON data for processing",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "str_data": {
                    "type": "string",
                    "description": "The string data to be processed"
                  },
                  "int_data": {
                    "type": "integer",
                    "description": "The integer data to be processed"
                  }
                },
                "required": ["str_data", "int_data"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "example": {
                  "Received String": "example_string",
                  "Received Integer": 42
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {}
  }
}
```
