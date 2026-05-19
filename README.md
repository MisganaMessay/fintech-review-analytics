## PostgreSQL Database Setup

### Create Database

```sql
CREATE DATABASE fintech_reviews;
```

### Run Database Schema

```bash
"C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d fintech_reviews -f sql/schema.sql
```

### Load Processed Data

```bash
python scripts/load_to_postgres.py
```

## Database Schema

### banks Table

| Column | Type |
|---|---|
| bank_id | SERIAL PRIMARY KEY |
| bank_name | VARCHAR(100) |

### reviews Table

| Column | Type |
|---|---|
| review_id | SERIAL PRIMARY KEY |
| bank_id | INTEGER |
| review_text | TEXT |
| rating | INTEGER |
| review_date | DATE |
| sentiment_label | VARCHAR(20) |
| sentiment_score | FLOAT |