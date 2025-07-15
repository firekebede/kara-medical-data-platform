-- models/staging/stg_telegram_messages.sql
with source as (
  select * from raw.telegram_messages
)
select
  id,
  message,
  date,
  channel,
  sender_id,
  has_media,
  media_path,
  length(message) as message_length
from source
where message is not null;
