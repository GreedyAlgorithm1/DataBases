/*Transactions/bills can't be issued when given bar is closed*/
DROP FUNCTION IF EXISTS check_bill_time
CREATE FUNCTION check_bill_time(timeOfIssue int, barID int) return varchar(50)
BEGIN
	if(
		exists(
			select b.bar
			from bars b JOIN operationHours oH on b.barID = oH.barID
			where b.barID = barID and timeOfIssue < b.CloseTime and timeOfIssue > b.Opentime 
			)
		)return 'True'
	else
	return 'False'
END;

/*drinkers can't frequent bars in different state*/
/*NOTE THIS IS ONLY DONE ON NEW INPUTS*/
DROP FUNCTION IF EXISTS check_state
CREATE FUNCTION check_state(drinker_input varchar, barState varchar) RETURNS VARCHAR(50)
BEGIN
	if ( 
		EXISTS (
			select state
			from drinkers
			where drinker_input = name and barState = state
		)
	) return 'True'
	else 
	return 'False'
END;
 
/*beer heirarchy established*/
/*
DROP FUNCTION IF EXISTS check_beer_order
CREATE FUNCTION check_beer_order(beer varchar) RETURNS VARCHAR
BEGIN
	if
*/