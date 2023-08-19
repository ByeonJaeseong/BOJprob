import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int i=0; i<T; i++) {
			int x=sc.nextInt();
				String str1=sc.next();
				String[] arrayString= new String[str1.length()*x];
				
				for(int l=0; l<str1.length(); l++) {
					String str2 = str1.substring(l,l+1);
				for(int k=0; k<x; k++) {
					arrayString[l*x+k]= str2;}
				}
				for(int m=0; m<str1.length()*x; m++) {
				System.out.print(arrayString[m]);
				}
            System.out.println();

				
			
		}
				
				
		

	}

}
