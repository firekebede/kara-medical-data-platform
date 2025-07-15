-- models/marts/dim_dates.sql
with dates as (
  select distinct date::date as date
  from {{ ref('stg_telegram_messages') }}
)
select
  date,
  extract(dow from date) as day_of_week,
  extract(week from date) as week_number,
  extract(month from date) as month,
  extract(year from date) as year
from dates;
