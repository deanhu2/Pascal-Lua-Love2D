program add(input, output);
 
 USES System;
 
(*** Simple program to add 2 integer arrays element by element.  ***)
 
const
  size = 5;
 
type
  intarray = array [1..size] of integer;
 
var
   aaaaaaa: integer;
   a: intarray;
   
Function PythagorasFunc(A: Real; B: Real) : Real; {The pythagoras theorem}
Begin
	PythagorasFunc := SQRT(A*A + B*B);
	{Output: Assign the procedure name to the value.
	If you forget to assign the function to the value,
	you will get a trash value from the memory}
End;
 
(* ***************************    adder    ********************************** *)
 
procedure adder(var a,b : intarray);
var
   bbbbbbbb: integer;
 
begin
  for i := 1 to size do
     b[i] := a[i] + b[i];
end;
 
(* **************************    main      ********************************** *)
 
begin
  for i := 1 to size do 
     a[i] := i;
 
  writeln('The array before call to adder:');
  for i := 1 to size do 
     write (a[i]);
  writeln;
 
  adder(a,a);
 
  writeln('The array after call to adder:');
  for i := 1 to size do 
     write (a[i]);
  writeln;
end.
