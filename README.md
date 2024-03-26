
# Trade and Material Assets (TMA)


This project is a system designed to facilitate coordination of goods and purchase requests within a company. It serves two main user roles:

Coordinator: The coordinator has access to functionalities such as navigating through the list of goods and purchase requests. They can sort table rows, apply filters, search for specific items, and perform actions like adding, updating, or removing goods from the list. Additionally, they can view detailed descriptions of goods associated with purchase requests, confirm or reject requests, and provide comments for refusals.

Company Employee: The company employee interacts with the system primarily from the home page, where they can access a list of all goods. Similar to the coordinator, they can sort, filter, and search for items. They can also place orders by filling out a form with details such as item name, quantity, price, and optional comment. After submitting an order, the system displays a confirmation message. Employees can also add items to an existing request, with the system providing feedback upon completion.

This project aims to streamline the procurement process within the company, providing a user-friendly interface for both coordinators and employees to manage goods and purchase requests efficiently.
## Acknowledgements
I would like to express my gratitude to the following individuals and resources for their contributions to this project:

 - [Django Documentation: For providing comprehensive guidance on Django web development.](https://docs.djangoproject.com/en/5.0/)
 - [Stack Overflow: For the wealth of knowledge shared by the developer community.](https://stackoverflow.com/)
 - [Python Package Index (PyPI): For hosting invaluable Python packages used in this project](https://pypi.org/)

These resources have been instrumental in the development process, providing guidance, solutions, and inspiration along the way. Their contributions are deeply appreciated.





## Authors

- [@pumpezny](https://github.com/pumpezny)


## Diogramms

user_user_permissions
-----------------------------------------------------
|   id (primary key)   |   user_id   |   permission_id   |
-----------------------------------------------------
|         ...           |     ...     |        ...        |
-----------------------------------------------------

Индексы:
1. user_user_permissions_permission_id_9deb68a3 (индекс по полю "permission_id")
2. user_user_permissions_user_id_ed4a47ea (индекс по полю "user_id")

Ограничения:
1. primary_key: user_user_permissions_pkey (первичный ключ для поля "id")
2. unique_constraint: user_user_permissions_user_id_permission_id_7dc6e2e0_uniq (уникальное ограничение для комбинации полей "user_id" и "permission_id")

Связи:
- Внешний ключ user_user_permission_permission_id_9deb68a3_fk_auth_perm указывает на поле "id" таблицы "auth_permission".
- Внешний ключ user_user_permissions_user_id_ed4a47ea_fk_user_id указывает на поле "id" таблицы "user".


user_groups
-----------------------------------------------------
|   id (primary key)   |   user_id   |   group_id   |
-----------------------------------------------------
|         ...           |     ...     |     ...      |
-----------------------------------------------------

Индексы:
1. user_groups_group_id_b76f8aba (индекс по полю "group_id")
2. user_groups_user_id_abaea130 (индекс по полю "user_id")

Ограничения:
1. primary_key: user_groups_pkey (первичный ключ для поля "id")
2. unique_constraint: user_groups_user_id_group_id_40beef00_uniq (уникальное ограничение для комбинации полей "user_id" и "group_id")

Связи:
- Внешний ключ user_groups_group_id_b76f8aba_fk_auth_group_id указывает на поле "id" таблицы "auth_group".
- Внешний ключ user_groups_user_id_abaea130_fk_user_id указывает на поле "id" таблицы "user".


user
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|   id (primary key)   |   password   |   last_login   |   is_superuser   |   username   |   first_name   |   last_name   |   email   |   is_staff   |   is_active   |   date_joined   |   image   |   phone_number   |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|         ...           |     ...      |       ...      |       ...        |     ...      |      ...       |      ...      |    ...    |     ...      |      ...      |       ...       |    ...    |        ...       |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Индексы:
1. user_username_cf016618_like (индекс по полю "username" для частичного совпадения)

Ограничения:
1. primary_key: user_pkey (первичный ключ для поля "id")
2. unique_constraint: user_username_key (уникальное ограничение для поля "username")

Связи:
- Внешний ключ cart_user_id_1361a739_fk_user_id указывает на поле "id" таблицы "cart".
- Внешний ключ django_admin_log_user_id_c564eba6_fk_user_id указывает на поле "id" таблицы "django_admin_log".
- Внешний ключ order_user_id_e323497c_fk_user_id указывает на поле "id" таблицы "order".
- Внешний ключ user_groups_user_id_abaea130_fk_user_id указывает на поле "id" таблицы "user_groups".
- Внешний ключ user_user_permissions_user_id_ed4a47ea_fk_user_id указывает на поле "id" таблицы "user_user_permissions".


status
----------------------------------------------------
|   id (primary key)   |   main   |   slug        |
----------------------------------------------------
|         ...           |   ...    |   ...         |
----------------------------------------------------

Индексы:
1. status_name_68e1d769_like (индекс по полю "main" для частичного совпадения)
2. status_slug_e39cdd45_like (индекс по полю "slug" для частичного совпадения)

Ограничения:
1. primary_key: status_pkey (первичный ключ для поля "id")
2. unique_constraint: status_name_key (уникальное ограничение для поля "main")
3. unique_constraint: status_slug_key (уникальное ограничение для поля "slug")

Связи:
- Внешний ключ product_status_id_abfe03fb_fk_status_id указывает на поле "id" таблицы "status".


product
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|   id (primary key)   |   name   |   slug   |   description   |   quantity   |   price   |   discount   |   storageLocation   |   contactPerson   |   image   |   category_id   |   status_id   |   unitsOfMeasurement   |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|         ...           |   ...    |   ...    |      ...        |     ...      |   ...     |     ...      |         ...         |        ...        |    ...    |       ...       |      ...      |          ...          |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Индексы:
1. product_category_id_640030a0 (индекс по полю "category_id")
2. product_name_af48c283_like (индекс по полю "name" для частичного совпадения)
3. product_slug_c4732ed0_like (индекс по полю "slug" для частичного совпадения)
4. product_status_id_abfe03fb (индекс по полю "status_id")
5. product_unitsOfMeasurement_id_3bcaaf63 (индекс по полю "unitsOfMeasurement")

Ограничения:
1. primary_key: product_pkey (первичный ключ для поля "id")
2. unique_constraint: product_name_key (уникальное ограничение для поля "name")
3. unique_constraint: product_slug_key (уникальное ограничение для поля "slug")
4. check: product_quantity_check (проверка на количество)

Связи:
- Внешний ключ product_category_id_640030a0_fk_category_id указывает на поле "id" таблицы "category".
- Внешний ключ product_status_id_abfe03fb_fk_status_id указывает на поле "id" таблицы "status".
- Внешний ключ product_unitsOfMeasurement_id_3bcaaf63_fk_UnitOfMeasurement_id указывает на поле "id" таблицы "UnitOfMeasurement".


order_item
-----------------------------------------------------------------------------------------------------------------------------
|   id (primary key)   |   name   |   price   |   quantity   |   created_timestamp   |   order_id   |   product_id   |
-----------------------------------------------------------------------------------------------------------------------------
|         ...           |   ...    |   ...     |     ...     |         ...           |     ...      |      ...       |
-----------------------------------------------------------------------------------------------------------------------------

Индексы:
1. order_item_order_id_0ca9e92e (индекс по полю "order_id")
2. order_item_product_id_62a1cc4c (индекс по полю "product_id")

Ограничения:
1. primary_key: order_item_pkey (первичный ключ для поля "id")
2. check: order_item_quantity_check (проверка на количество)

Связи:
- Внешний ключ order_item_order_id_0ca9e92e_fk_order_id указывает на поле "id" таблицы "order".
- Внешний ключ order_item_product_id_62a1cc4c_fk_product_id указывает на поле "id" таблицы "product".


order
-----------------------------------------------------------------------------------------------------------------------------
|   id (primary key)   |   created_timestamp   |   phone_number   |   requires_delivery   |   delivery_address   |   payment_on_get   |   is_paid   |   status   |   user_id   |
-----------------------------------------------------------------------------------------------------------------------------
|         ...           |         ...           |       ...         |         ...           |         ...          |       ...         |     ...     |     ...    |     ...     |
-----------------------------------------------------------------------------------------------------------------------------

Индексы:
1. order_user_id_e323497c (индекс по полю "user_id")

Ограничения:
1. primary_key: order_pkey (первичный ключ для поля "id")

Связи:
- Внешний ключ order_user_id_e323497c_fk_user_id указывает на поле "id" таблицы "user".


django_admin_log
----------------------------------------------------------------------------------------------------------------
|   id (primary key)   |   action_time   |   object_id   |   object_repr   |   action_flag   |   change_message   |   content_type_id   |   user_id   |
----------------------------------------------------------------------------------------------------------------
|         ...           |       ...       |      ...      |       ...       |       ...       |         ...        |          ...        |     ...     |
----------------------------------------------------------------------------------------------------------------

Индексы:
1. django_admin_log_content_type_id_c4bce8eb (индекс по полю "content_type_id")
2. django_admin_log_user_id_c564eba6 (индекс по полю "user_id")

Ограничения:
1. primary_key: django_admin_log_pkey (первичный ключ для поля "id")
2. check: django_admin_log_action_flag_check (проверка на флаг действия)

Связи:
- Внешний ключ django_admin_log_content_type_id_c4bce8eb_fk_django_co указывает на поле "id" таблицы "django_content_type".
- Внешний ключ django_admin_log_user_id_c564eba6_fk_user_id указывает на поле "id" таблицы "user".


category
----------------------------------------------
|   id (primary key)   |   name   |   slug    |
----------------------------------------------
|         ...           |   ...    |   ...     |
----------------------------------------------

Индексы:
1. category_name_15cb1e98_like (индекс по полю "name")
2. category_slug_fd4fc841_like (индекс по полю "slug")

Ограничения:
1. primary_key: category_pkey (первичный ключ для поля "id")
2. unique_constraint: category_name_key (уникальное ограничение для поля "name")
3. unique_constraint: category_slug_key (уникальное ограничение для поля "slug")

Связи:
- Внешний ключ product_category_id_640030a0_fk_category_id указывает на поле "id" таблицы "product".


cart
--------------------------------------------------------------------------------------------------------
|   id (primary key)   |   quantity   |   session_key   |   created_timestamp   |   product_id   |   user_id   |
--------------------------------------------------------------------------------------------------------
|         ...           |     ...      |       ...       |          ...          |       ...      |     ...     |
--------------------------------------------------------------------------------------------------------

Индексы:
1. cart_product_id_508e72da (индекс по полю "product_id")
2. cart_user_id_1361a739 (индекс по полю "user_id")

Ограничения:
1. primary_key: cart_pkey (первичный ключ для поля "id")
2. check: cart_quantity_check (проверка на количество)

Связи:
- Внешний ключ cart_product_id_508e72da_fk_product_id указывает на поле "id" таблицы "product".
- Внешний ключ cart_user_id_1361a739_fk_user_id указывает на поле "id" таблицы "user".


UnitOfMeasurement
--------------------------------------------------
|   id (primary key)   |   name   |   slug       |
--------------------------------------------------
|         ...          |   ...    |   ...        |
--------------------------------------------------

Индексы:
1. UnitOfMeasurement_name_5d5de659_like (поиск по полю "name")
2. UnitOfMeasurement_slug_3126b8b8_like (поиск по полю "slug")

Ограничения:
1. primary_key: UnitOfMeasurement_pkey (первичный ключ для поля "id")
2. unique_constraint: UnitOfMeasurement_name_key (уникальное ограничение для поля "name")
3. unique_constraint: UnitOfMeasurement_slug_key (уникальное ограничение для поля "slug")

Связи:
- Связь с таблицей "product" по полю "product_unitsOfMeasurement_id" с внешним ключом, указывающим на поле "id" таблицы "UnitOfMeasurement".

