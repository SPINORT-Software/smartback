/***
  This query will show all the calibration sessions for a user
 */

 select * from infra_session where user_id = 4 and type = 'CALIBRATION';