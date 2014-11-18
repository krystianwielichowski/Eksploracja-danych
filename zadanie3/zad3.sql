use Northwind
go
create view Wielichowski_WymiarDostawca as (
	select SupplierID, CompanyName, City, Country from Suppliers)


Create view Wielichowski_WymiarPrudukt as (
	select Products.ProductID, Products.ProductName, Products.CategoryID,
		Categories.CategoryName from Products inner join Categories on 
		(Products.CategoryID = Categories.CategoryID))

Create  view Wielichowski_FaktyProdukty as (
select ProductID, SupplierID, UnitsInStock from products)


drop view Wielichowski_WymiarDostawca, Wielichowski_WymiarPrudukt, Wielichowski_FaktyProdukty


Select * into Wielichowski_WymiarDostawca from (
	select SupplierID, CompanyName, City, Country from Suppliers) as w

Select * into Wielichowski_WymiarPrudukt from (
	select Products.ProductID, Products.ProductName, Products.CategoryID,
		Categories.CategoryName from Products inner join Categories on 
		(Products.CategoryID = Categories.CategoryID))

Select * into Wielichowski_FaktyProdukty from (
	select ProductID, SupplierID, UnitsInStock from products)

