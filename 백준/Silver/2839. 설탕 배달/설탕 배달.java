import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int a=N;
		int b=0;
		while(true) {
		if(a%5==0) {
			b=b+a/5;
			a=0;
			
		}else {
			a-=3;
			b++;
			
		}
		if(a==0) {
			System.out.println(b);
			break;
		}else if(a<0){
			System.out.println(-1);
			break;
		}
		}
		
	}

}