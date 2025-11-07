
-- name: select_incident_by_status
-- record_class: IncidentRespModel
SELECT id, description, status, source, create_dt
FROM incidents
WHERE status = :status
;


-- name: insert_incident^
-- record_class: IncidentRespModel
INSERT INTO incidents (description, status, source, create_dt)
VALUES (
      :description
    , :status
    , :source
    , :create_dt
)
RETURNING id, description, status, source, create_dt
;

-- name: update_incident^
-- record_class: IncidentRespModel
UPDATE incidents
SET status = :status
WHERE id = :incident_id
RETURNING id, description, status, source, create_dt
;


