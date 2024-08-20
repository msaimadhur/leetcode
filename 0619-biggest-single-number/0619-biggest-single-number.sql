# Write your MySQL query statement below
with cte as (
    select num, count(num) as occurence
    from mynumbers
    group by num
)
select max(num) as num
from cte
where occurence = 1 or occurence is null
order by num desc
limit 1;