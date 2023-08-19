import java.util.*;
public class Main{
		public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int a,A,b;
		a = sc.nextInt();
		A = a;
		b = 1;
		count : for(int i=0; i<=100; i++) {
			if(A<10){
		            A = A + 10*A;
		        } else{
		                int decimal= (int)A/10;
		                int decimal1= A-9*decimal;
		                int decimal2= decimal1- ((int) decimal1/10)*10;
		                 A =  (A - decimal*10)*10 + decimal2;
		        }
			if(a==A) break count;
			
			++b;			
		}
	System.out.println(b);			
	}
}