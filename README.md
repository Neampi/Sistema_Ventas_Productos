# Sistema de Ventas de Productos

Sistema de ventas creado en Python, diseñado con QtDesigner, con el sistema de gestion de base de datos relacional SQL SERVER.

Implementacion de ComboBox, PushButton, DateEdit, TableWidget, etc, en cada ventana.

Las ventanas estan diseñadas en QtDesigner en la carpeta files_ui con terminaciones .ui y convertidas a python .py en la carpeta views

Las funcionalidades del programa estan en la carpeta controllers.

La conexion a la base de datos esta en db/conexion_sql.py

Ventanas Sesion, Home, Inventario, Compras, Ventas, Reportes, Avanzado, Configuracion

Cuenta con Inicio de Sesion vinculado con la base de datos para acceder.

En la ventana Inventario se pueden hacer busqueda de producto según el modelo a buscar.

En la ventana Compras se puede realizar nueva compra para añadir al Inventario y hacer busquedas ya sea por Fecha, Categoria, Marca y Modelo

En la ventana Venta se realiza el proceso de venta ingresando los datos del cliente, el tipo de pago y los productos en el boton "Buscar", y seguir con el boton "PROCESAR" para completar la venta.

En la ventana Reportes se visualiza las ventas realizadas con todo detalle segun vendedor a cargo, fecha, o producto, generando un reporte.

En la ventana Avanzado se podra realizar reportes con MATPLOTLIB.

En la ventana configuracion podra tener acceso el Administrador para modificar permisos y datos de todos los usuarios que esten registrados en la base de datos.








## Autor

- [@Neampi](https://github.com/Neampi)


## Imagenes

QT DESIGNER LOGIN

![Qt Designer LOGIN](https://previews.dropbox.com/p/thumb/AB0YV1rtHR689rpZJeg5K4wwy33vyegKVCRW_otQLXfh7XIpZt0FWKwU5rde_0YTi3q6cWkbq95E83zaDzP7JPwiI9DOu_DjGPFkGLx5lauh7INvPmn-DTR2GEoPNCVLnvD4JIwyfewL4bE4yYtqruS6AW1NfZTFJ_USi1ewnA1QTdCM-1juixGY64CGmAr8dh_zemO-ttisdnrk37me04dU27KGOOuelrdn16cArecES-rfj8Ww-psbqyHZky6LQpC-ISV2ZA_YbqRPb-zcEDCCO5xPaAOgV0alKvStghO6lqSshlvVyfexAoTTfaR_Ncb1Sjvu0mgsTfR-tKijMbff_4iOcDD9QR8GFWOwnAvU-NbbXMiLwkmVSfZs5jD17kA/p.png)

QT DESIGNER PRINCIPAL

![Qt Designer PRINCIPAL](https://previews.dropbox.com/p/thumb/AB0r-nhGtPuiBuDaSKXMFFTDUUzBegTLYnxCdl0wyoyDpe_8X-OdzapCgXkCyUHhrw3hHMta-aJxjnW192MAGQUynUUNerYRl27fj1BeAcMqmIbopvp8RYspZcY7GtzyY8ucA_Xh2JPxlqyek2_41-u8h92Nwt5G8SpyfgKXU04EokS7gPKLvecTNQjQbLhtC3CS9us7a-s2NNtdog-_jGODiqBKaq-kmTKg4dUSk2A2q9gccPjj1dtWgYnThNwApvpb82vEHXAFdmrWuhNxKVeKUjYSi_7JwXPaOPKFhjifUwK3h7PjDI8j25s7Ok-hIAycpvi5U1hzTHqSNyJ7qCcwPLhcTAQuPmujWuU52Ks64OQt5IbH6i1wZYa_uWBT0fI/p.png)

QT DESIGNER REGISTRO COMPRAS

![Qt Designer REGISTRO COMPRAS](https://previews.dropbox.com/p/thumb/AB2y63WbmqpZvb5L29E3TDIO-QDmgjWhsSFFtq9NLM54cvnofa8qCFtTxjx5AwiL6cblofL7jntEADb6vGZz0AiegyDMMpBtZpxi4-MbLtx56psH6fy1NOMkVNHBWWa4PY0vMLJyVxHAr0b58yyGZle1mHPDTZh-bQhIztCbY_Zsh0uMa2GUIzdUp44wrKYD2AEpsOGd6FfnnIXgrjwwjbnEQG65UD3ZnwMeJohL_kjw8bdZzDrVHtWdg_pkvuMTmcbOLYvv1m_OLwQBn424Y6r8B2vjY5uOZkkvU_YA6FN7wobhwmbqRAIt1HFXhR7TgPAuKzZKn5ejY5e76K845LRe3dS2w5XXwhA4yEybiRJIOLHYO4EOL5T0NIXfhRVIbpE/p.png)

QT DESIGNER SELECCION DE PRODUCTOS

![Qt Designer SELECCION PRODUCTOS](https://previews.dropbox.com/p/thumb/AB2oIPUbbvi8GZVXC4ucfnZM6eOh6IovAI8gRjwVXMhTwoDcqEO5TUqYkF885wT0ensyGGa_AderAYcbUoSbQ7FzKtst8sMsDItbi6pa29G661EGn1D-02Ph3vZC19hpVkJWq_UGCVMBETKV_3CRRZ6ZyiIp1G9bKHa7ZVemFpomllO60FQazT6ygAqX1I4zLncLF0BKKjYkkZkjnN_JXWIYvV5ZLNbpxmQrdjprQhem_jI1IPgmwIT1sSJnwfq4IZUJ0IFvi9nf1o25_MxdqC_zlD7fCVxDUgIvZmTdoVoad203N68yhXcnU2lnc2awbFlev52tkE0P03OG33cI-FOnEGm8DD7zAmNtadDC3EwelVJBibK6_yUb4hDTDz2o84E/p.png)

COMPRAS

![Qt Designer COMPRAS](https://previews.dropbox.com/p/thumb/AB1kdV4AyOLlqFjONrNJO_ka_WGtjGy3Hwrb0f3LYsileukrrxPjVOOldKfUETis2fCNJptKl20oyHDoPWEv5KTDgECmC5NFYV88sP4cqiRgYc6EeQI2InP_p_G4xZRgTP0MX2zrd-y3iNWSvErO2YW3bkrxhdLZjEZLksFZ0CZjSSkuUG_GcbgzPEx7RsYaEZD916CQDIQMtdnKGEyH4dujX3ZRDyyguZoN5FqNKR_ZloBcHYFv1XH1q6FbkEgnZjI9SSoNoEt9njTTuGae2KIiHwIVkY7TfWh0N-hbNGLMK2BZPrwWKcfvMUBpqhS2uGmxAIKYqK0Q9LNhPcsEzoMZbtjU9QsKos5YBe75bqX5AHWdMGnRTo11UvYIRdwE3wA/p.png)

INVENTARIO

![Qt Designer INVENTARIO](https://previews.dropbox.com/p/thumb/AB3ciOTSeTTGH5XhWXbkEij-ffaOQDTQKCO7B4fjLaKn0X_aQ59c9-Vlp9zx7O8mja3YeQ2MgUDiua-0tPhrgApxL6ccaxCQ7bmSgi_rAiMewuiev0GSAxQn8ktUHQ5sLER2CA8ReQpqw-R00xZRzbS7Y6F76In8CG7R84PvZwZ0UpH_Eo5b3Ad2xi1qQfzTpykjAOzC4EdB3YYt62o6jBTh7pqMm3gq7Pl8j8YFHXQFQi6pVFcVYkZApbVsOl0sN_31hgV9HVycvh34z4xoo6KXsydw8APQFmNoKQomqFt0r8edW74_1rn9fk_GPP111MjkPlnBIG7nfMpYJW_Td5G-5Rj0Mn-6hfT6ppUtVKS4YpnvzJGzGoYliegHXUOKiNg/p.png)

SELECCION DE PRODUCTOS

![Qt Designer SELECCION PRODUCTOS](https://previews.dropbox.com/p/thumb/AB0EUQpNZdIjDdTYh_lq2TC1ZJMwTdDAs5OEF8YK2NZ4z6Lh9xAX4nDL2bpCquI0D1AoyEDWODSYywcbfw10ZFG33pttAhWrMrpfSf-f0mle7BwPf7bD02iFX0CGIOP9NBusMBqtQifoz_fLhCLwf-uThpO7EiywgcNBjNbKDXU50zOp6MIOhcrHylmDU7USfXCHKzyYv3Ls6OgyEz7EKsdFCNSUCqEQpAwZyQARWBSwvYYaS4YOOXvIrHB2wGCvVPJQN539Y33njOy59pv78chpAeuqQueFxuGF8mDVYV7vrEYK6ay7TsmkeGRH-sXZ6f_TFmG1sL_vOZ2gbMw7j6AyMm3hfLXMNzh6nfkf7ITHYWgvDZl8zmvGVcW-dCKWEkc/p.png)

CONEXION A BASE DE DATOS

![Qt Designer CONEXION BD](https://previews.dropbox.com/p/thumb/AB3s9BiC9273iADoxMCkVJ1ZHXTy6dtx9-rT-ofe0u6sevoU8py1L7WRwBO9wsqTCM5BixBCARwRw15R1O5LHlxHNAUbPs93E6dK0_XIMbJVgpUF7gX86IAZf1J70XbmASiQLtOPKil80KrkXTEM0OSFDJBvkBBu5ZL2XCYFP6xlnhJz03msQ7z3UFIW7xAgRqVx0274i7Eh8r19IYk5wYrd53XP6gfnU2oB-6dvhCECcZ13ZPfwILZUimoD4gRSKhR87Rq7fj4X0qDEX0iQ_F-G86F7xAznJylJQ878ONK8MY7JWtwownHhojRWDJLvy1LV7-BouFngUZwLveizSiqZkczRrV2nUAkauFhav7Gh9pPU6yTW78AZzwSu_4xBt6o/p.png)
