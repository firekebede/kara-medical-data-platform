select
  d.message_id,
  d.detected_class,
  d.confidence
from raw.image_detections d
join {{ ref('fct_messages') }} m
  on d.message_id = m.id
