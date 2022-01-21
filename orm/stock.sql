/*"日期","收盘","开盘","高","低","交易量","涨跌幅"*/
CREATE TABLE `stocks` (
	`stock_code` varchar(12) NOT NULL,
	`stock_date` varchar(255) COLLATE utf8_bin NOT NULL,
	`close` float NOT NULL,
	`open` float NOT NULL default 0,
	`high_day` float NOT NULL default 0,
	`low_day` float NOT NULL default 0,
	`volume` float NOT NULL default 0,
	`amplitude` float NOT NULL default 0,
	PRIMARY KEY (`stock_code`,`stock_date`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
