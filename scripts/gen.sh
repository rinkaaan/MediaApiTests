WORKPLACE="$HOME/workplace/Media"
WORKSPACE="$WORKPLACE/MediaApiTests"
SCHEMA_PATH="$WORKPLACE/MediaApi/api/openapi.yaml"

(
  cd "$WORKSPACE"
  rm -rf openapi_client
  mkdir -p openapi_client

  cd openapi_client
  npx @openapitools/openapi-generator-cli generate -i "$SCHEMA_PATH" -g python --skip-validate-spec
  pip install .
)

rm -rf openapi_client
