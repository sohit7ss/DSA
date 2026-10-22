SELECT
    id
FROM (
    SELECT
        id,
        temperature,
        recordDate,
        LAG(temperature) OVER (ORDER BY recordDate) AS PreviousTemperature,
        LAG(recordDate) OVER (ORDER BY recordDate) AS PreviousDate
    FROM Weather
) AS w
WHERE PreviousTemperature < temperature
    AND DATEDIFF(day, PreviousDate, recordDate) = 1;
