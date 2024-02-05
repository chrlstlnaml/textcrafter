-- Publication's rating we calculate using this formula: "number_of_positive_votes - number_of_negative_votes".
-- The rating is determined by summing the values of votes associated with the publication, as each positive
-- vote (like) contributes +1, each negative vote (dislike) contributes -1, and each revoked vote contributes 0.

CREATE VIEW vw_publication AS
SELECT
    p.id,
    p.text,
    p.public_date,
    p.author_id,
    u.username AS author,
    COALESCE(SUM(v.value), 0) AS rating,
    COUNT(CASE WHEN v.value <> 0 THEN 1 END) AS vote_count
FROM publication p
LEFT JOIN vote v ON p.id = v.publication_id
LEFT JOIN auth_user u ON p.author_id = u.id
GROUP BY p.id, p.text, p.public_date, p.author_id;