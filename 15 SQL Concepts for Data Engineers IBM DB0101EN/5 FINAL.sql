SELECT SC.NAME_OF_SCHOOL , SC.COMMUNITY_AREA_NAME ,CD.HARDSHIP_INDEX  
FROM CHICAGOPUBLICSCHOOLS SC
INNER JOIN CHICAGOCENSUSDATA CD
ON SC.COMMUNITY_AREA_NUMBER = CD.HARDSHIP_INDEX
AND CD.HARDSHIP_INDEX > 56

SELECT CR.* , CN.COMMUNITY_AREA_NAME
FROM CHICAGOCRIMEDATA CR
LEFT JOIN CHICAGOCENSUSDATA CN
ON CN.COMMUNITY_AREA_NUMBER = CR.COMMUNITY_AREA_NUMBER
WHERE (LOCATION_DESCRIPTION LIKE '%SCHOOL%')
OR 
(DESCRIPTION LIKE '%SCHOOL%')


CREATE VIEW SCHOOLS
AS 
SELECT 
SC.NAME_OF_SCHOOL AS School_Name,
SC.Safety_Icon AS Safety_Rating,
SC.Family_Involvement_Icon AS Family_Rating,
SC.Environment_Icon AS Environment_Rating,
SC.Instruction_Icon AS Instruction_Rating,
SC.Leaders_Icon AS 	Leaders_Rating,
SC.Teachers_Icon AS Teachers_Rating
FROM CHICAGOPUBLICSCHOOLS SC


SELECT *
FROM SCHOOLS
WHERE SAFETY_RATING Like '%Strong%'
AND FAMILY_RATING Like '%Strong%'


--#SET TERMINATOR @
CREATE PROCEDURE UPDATE_LEADERS_SCORE                    -- Name of this stored procedure routine

LANGUAGE SQL                                                -- Language used in this routine 
MODIFIES SQL DATA                                           -- This routine will only write/modify data in the table

BEGIN

        DECLARE SQLCODE INTEGER DEFAULT 0;                  -- Host variable SQLCODE declared and assigned 0
        DECLARE retcode INTEGER DEFAULT 0;                  -- Local variable retcode with declared and assigned 0
        DECLARE CONTINUE HANDLER FOR SQLEXCEPTION           -- Handler tell the routine what to do when an error or warning occurs
        SET retcode = SQLCODE;                              -- Value of SQLCODE assigned to local variable retcode
        
        UPDATE CHICAGOPUBLICSCHOOLS
        SET LEADERS_ICON = 'Very strong'
        WHERE 80 <= LEADERS_SCORE <=99;
        
        UPDATE CHICAGOPUBLICSCHOOLS
        SET LEADERS_ICON = 'Strong'
        WHERE 60 <= LEADERS_SCORE <=79;
        

        
        IF retcode < 0 THEN                                  --  SQLCODE returns negative value for error, zero for success, positive value for warning
            ROLLBACK WORK;
        
        ELSE
            COMMIT WORK;
        
        END IF;
        
END
@                                                            -- Routine termination character


