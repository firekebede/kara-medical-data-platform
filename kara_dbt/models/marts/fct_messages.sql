-- models/marts/fct_messages.sql
select
  s.id,
  s.date::date as date,
  s.channel,
  s.sender_id,
  s.message_length,
  s.has_media,
  s.media_path
from {{ ref('stg_telegram_messages') }} s
