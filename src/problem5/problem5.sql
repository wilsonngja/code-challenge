SELECT balance.address FROM balance
INNER JOIN trades ON trades.address = balance.address 
AND (CASE 
	 WHEN balance.denom = 'usdc' THEN 
	 	CASE 
		 	WHEN (0.000001*balance.amount > 500) AND (trades.block_height > 730000) THEN true ELSE false END
	 
	 WHEN balance.denom = 'swth' THEN 
	 	CASE
	 		WHEN (0.00000005*balance.amount > 500 AND trades.block_height > 730000) THEN true ELSE false END
	 WHEN balance.denom = 'tmz' THEN 
	 	CASE
	 		WHEN (0.003*balance.amount > 500 AND trades.block_height > 730000) THEN true ELSE false END
	ELSE false END);

		