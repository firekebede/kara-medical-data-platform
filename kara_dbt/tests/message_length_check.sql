-- Ensure no messages are too long
select *
from {{ ref('fct_messages') }}
where message_length > 4000;
