# Loan Data Model Design

## Task

Loan Lifecycle Process

- Small​ ​businesses (​borrowers​) can apply for loans
- If the application is successful, it is listed on a marketplace where multiple investors ​can
fund a part of the loan (​loan part​), until the full amount of the loan has been funded.
- Once a loan has been fully funded, the ​borrower​ receives the full amount and a monthly
​repayment schedule​ is generated.
- The ​borrower​ then makes a repayment according to the schedule, that repayment gets
distributed between ​investors​ according to the value on each loan part.

Requirements

1. Design data model as a database schema to support analytics
2. The schema should capture key data points from above, plus any others that you think
are useful
3. Provide reasoning for your design decisions.

## Solution

After analyzing the given loan lifecycle process, the following database schema has been designed to support analytics.

```
+-----------------+     +---------+      +-------------+
|    Borrowers    |     |  Loans  |      | Investors   |
+-----------------+     +---------+      +-------------+
| borrower_id     |<--- | loan_id | ---> | investor_id |
| name            |     | amount  |      | name        |
| address         |     | rate    |      | address     |
| contact_details |     | term    |      | contact     |
+-----------------+     +---------+      +-------------+
          |                    |                |
          |                    |                |
          |                    |                |
          |                    |                |
          |               +-----------+         |
          |               | Loan Parts|         |
          |               +-----------+         |
          |               | part_id   | <-------+
          +-------------- | loan_id   |
                          | amount    |
                          | status      |
                          | investor_id |
                          +-----------+
                                      |
                                      |
                                      |
                                      |
                                      |
                                      |
                             +---------------+
                             |  Repayments   |
                             +---------------+
                             | repayment_id  |
                             | loan_id       |
                             | borrower_id   |
                             | amount        |
                             | date          |
                             | status        |
                             +---------------+
```

Explanation of the Data Model:

The database schema has been designed with five main tables:

**Borrowers**: This table contains the details of the borrowers who have applied for loans. It includes the borrower's unique ID, name, address, contact details, and other relevant information.

**Loans**: This table contains the details of the loans that have been listed on the marketplace. It includes the unique loan ID, the borrower ID, the loan amount, the interest rate, and the loan term.

**Investors**: This table contains the details of the investors who have funded the loans. It includes the unique investor ID, name, address, contact details, and other relevant information.

**Loan Parts**: This table contains the details of the loan parts that investors have funded. It includes the unique loan part ID, the loan ID, the investor ID, the amount invested, and the status (funded or not funded).

**Repayments**: This table contains the details of the monthly repayments made by the borrowers. It includes the unique repayment ID, the loan ID, the borrower ID, the repayment amount, the repayment date, and the status (paid or not paid).

The data model has been designed to capture key data points from the loan lifecycle process. It includes all the necessary information related to borrowers, loans, investors, loan parts, and repayments. The following are the reasons behind each design decision:

The Borrowers, Loans, and Investors tables are the primary tables in the data model because they contain the core information related to the loan lifecycle process.

The Loans table contains the loan amount, interest rate, and loan term. These are the key data points that investors would consider before funding a loan.

The Loan Parts table captures the details of the loan parts that investors have funded. It includes the amount invested and the status of the loan part.

The Repayments table captures the monthly repayments made by the borrowers. It includes the repayment amount, repayment date, and status of the repayment.

All tables have unique IDs to ensure data integrity and easy retrieval of information.

Relationships have been established between the tables using foreign keys to ensure data consistency.

The data model allows for easy aggregation and analysis of data for reporting and analytics purposes.

Overall, this database schema provides a comprehensive view of the loan lifecycle process and enables effective analysis of the data for various purposes.


Example of the SQL code:

```sql
CREATE TABLE Borrowers (
  borrower_id INT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  contact_details VARCHAR(255)
);

CREATE TABLE Loans (
  loan_id INT PRIMARY KEY,
  borrower_id INT,
  amount DECIMAL(10, 2),
  rate DECIMAL(4, 2),
  term INT,
  FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id)
);

CREATE TABLE Investors (
  investor_id INT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  contact VARCHAR(255)
);

CREATE TABLE Loan_Parts (
  part_id INT PRIMARY KEY,
  loan_id INT,
  investor_id INT,
  amount DECIMAL(10, 2),
  status VARCHAR(255),
  FOREIGN KEY (loan_id) REFERENCES Loans(loan_id),
  FOREIGN KEY (investor_id) REFERENCES Investors(investor_id)
);

CREATE TABLE Repayments (
  repayment_id INT PRIMARY KEY,
  loan_id INT,
  borrower_id INT,
  amount DECIMAL(10, 2),
  date DATETIME,
  status VARCHAR(255),
  FOREIGN KEY (loan_id) REFERENCES Loans(loan_id),
  FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id)
);
```
