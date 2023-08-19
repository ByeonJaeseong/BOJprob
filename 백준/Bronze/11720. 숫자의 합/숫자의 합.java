import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int inputInteger = sc.nextInt();
		String str=sc.next();
		
		int sum = 0;
		for(int i=0; i<inputInteger; i++) {
			String str1= str.substring(i,i+1);
			
			sum = sum + Integer.parseInt(str1);
		}
		System.out.println(sum);

	}

}
