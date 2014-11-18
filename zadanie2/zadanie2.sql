use Northwind
select EmployeeID, LastName, FirstName, Region from employees
where Region is NULL

select ProductName, UnitPrice from Products
where UnitPrice = (select  max(UnitPrice) from Products)
Union
select ProductName, UnitPrice from Products
where UnitPrice = (select  min(UnitPrice) from Products)
order by ProductName

Select ProductName, UnitPrice from Products
where UnitPrice > (select avg(UnitPrice) from Products)

select sum(freight) as Suma_frachtu from Orders


select Products.ProductName from Products
Inner join [Order Details] on Products.ProductID = [Order Details].ProductID
where [Order Details].OrderID in (select OrderID from Orders
Where (Datename(dw, OrderDate) = 'Saturnday') or (Datename(dw, OrderDate) = 'Sunday'))

select CategoryID, avg(UnitPrice) from Products
Group by CategoryID

Select * from Orders

select CustomerID, sum(select unitPrice*Quantity - Discount from [Order Details]) 
from Orders
group by CustomerID



drop view WykazZamowien
Create view WykazZamowien as
(select OrderID, 
sum(unitPrice*Quantity - Discount) as sumaZamowienia
from [Order Details]
group by OrderID)

Create view WykazKlientow as
(Select Orders.CustomerID, sum(WykazZamowien.sumaZamowienia) as SumaZamowien from Orders
Inner Join WykazZamowien on Orders.OrderID = WykazZamowien.OrderID
group by Orders.CustomerID)

Select Customers.CompanyName, WykazKlientow.SumaZamowien from Customers
inner join WykazKlientow on Customers.CustomerID = WykazKlientow.CustomerID

create view WykazProduktow as
(Select ProductID, Count(ProductID) as IloscZamowionych  
from [Order Details]
group by ProductID)

select Products.ProductName, WykazProduktow.IloscZamowionych from
Products inner join WykazProduktow on Products.ProductID = WykazProduktow.ProductID