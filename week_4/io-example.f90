program io_example
   implicit none
   real :: x, y(10)
   integer :: i

   do i = 1, 10
      x = float(i)
      y(i) = x**1/3 + 3*i
   end do

   !! good idea to open and close files with filenames
   !
   write(20,11) (y(i), i=1,10)
11 format(10(F5.1,1x))

end program
