# Política de Seguridad – CanSat Ajolote

## Reporte de Vulnerabilidades

Si encuentras una vulnerabilidad o una falla de seguridad en el código, agradeceremos que la reportes de forma responsable para poder solucionarla de inmediato.

### Contacto
Por favor, reporta los hallazgos a:

**William Enrique Padilla Vivero**  
willipadilla@proton.me  
Asunto: "Reporte de seguridad – CanSat Ajolote"

No reveles públicamente la vulnerabilidad hasta que hayamos tenido la oportunidad de analizarla y aplicar una solución.

## Alcance

Este proyecto no maneja datos sensibles ni personales. Sin embargo, las siguientes áreas podrían ser sensibles:

- Transmisión inalámbrica entre CanSat y estación base
- Integridad de los datos almacenados en MicroSD
- Comunicación con bases de datos externas (MongoDB/DynamoDB)

## Buenas prácticas esperadas

- No subir archivos con claves, tokens o configuraciones privadas
- Evitar el uso de contraseñas hardcodeadas en el firmware
- Usar conexiones cifradas (cuando sea posible en implementaciones futuras)
