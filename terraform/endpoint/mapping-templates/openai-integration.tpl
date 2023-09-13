## see https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
{
  "model": "$input.path('$.model')",
  "end_point": "${mapping_end_point}",
  "messages": [
    {"role": "system", "content": "${mapping_role_system_content}"},
    {"role": "user", "content": "$input.path('$.input_text')"}
    ]
}