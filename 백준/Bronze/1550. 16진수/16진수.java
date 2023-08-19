import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String arr = sc.next();
		int a=0;
		for(int i=0; i<arr.length(); i++) {
			switch(arr.charAt(i)) {
			case '0': 
				a=a+square(16,arr.length()-i-1)*0;
				break;
			case '1':
				a=a+square(16,arr.length()-i-1)*1;
				break;
			case '2':
				a=a+square(16,arr.length()-i-1)*2;
				break;
			case '3':
				a=a+square(16,arr.length()-i-1)*3;
				break;
			case '4':
				a=a+square(16,arr.length()-i-1)*4;
				break;
			case '5':
				a=a+square(16,arr.length()-i-1)*5;
				break;
			case '6':
				a=a+square(16,arr.length()-i-1)*6;
				break;
			case '7':
				a=a+square(16,arr.length()-i-1)*7;
				break;
			case '8':
				a=a+square(16,arr.length()-i-1)*8;
				break;
			case '9':
				a=a+square(16,arr.length()-i-1)*9;
				break;
			case 'A':
				a=a+square(16,arr.length()-i-1)*10;
				break;
			case 'B':
				a=a+square(16,arr.length()-i-1)*11;
				break;
			case 'C':
				a=a+square(16,arr.length()-i-1)*12;
				break;
			case 'D':
				a=a+square(16,arr.length()-i-1)*13;
				break;
			case 'E':
				a=a+square(16,arr.length()-i-1)*14;
				break;
			case 'F':
				a=a+square(16,arr.length()-i-1)*15;
				break;
			}
			
		}
		System.out.println(a);
		
	}

	public static int square(int n, int m) {
		int a=1;
		for(int i=0; i<m;i++) {
			a*=n;
		}
		return a;
	}
}
