create database banks_portal;

create table accounts (
accountID int not null unique auto_increment primary key,
ownerName varchar (45) Not Null,
owner_ssn int not null,
balance decimal (10,2) default 0.00,
account_status varchar (45)
);

create table Transactions (
transactionId int not null unique auto_increment primary key,
accountID int not null,
transactionType varchar (45) not null,
transactionAmount decimal (10,2) not null,
foreign key (accountID)
references accounts(accountID)
);

insert into accounts (ownerName, owner_ssn, balance, account_status)
values
("Maria Jozef", 123456789,10000.00, "active"),
("Linda Jones", 987654321, 2600.00, "inactive"),
("John McGrail", 222222222, 100.50, "active"),
("Patty Luna", 111111111, 509.75, "inactive");

insert into Transactions (accountID, transactionType, transactionAmount)
values 
(1, "deposit", 650.98),
(3, "withdraw", 899.87),
(3, "deposit", 350.00);

DELIMITER //
create procedure accountTransactions(accountID int)
BEGIN
	select *
    from Transactions
    where accountID = Transactions.accountID;
END //
DELIMITER ;

call accountTransactions(3)

DELIMITER //
create procedure deposit(accountID int, amount decimal(10,2))
BEGIN
	insert into Transactions (accountID, transactionType, transactionAmount)
    values (accountID, 'deposit', amount);
    
    update accounts
    set balance = balance + amount
    where accountID = accountID;
END //
DELIMITER ;

DELIMITER //
create procedure withdraw(accountID int, amount decimal(10,2))
BEGIN
	insert into Transactions (accountID, transactionType, transactionAmount)
    values (accountID, 'withdraw', amount);
    
    update accounts
    set balance = balance - amount
    where accountID = accountID;
END //
DELIMITER ;

select * from accounts