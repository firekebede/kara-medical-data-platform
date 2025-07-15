-- models/marts/dim_channels.sql
select distinct
  channel as channel_name,
  min(date) as first_seen,
  max(date) as last_seen
from {{ ref('stg_telegram_messages') }}
group by channel;

