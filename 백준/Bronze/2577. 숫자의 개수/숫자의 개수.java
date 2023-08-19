import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A =sc.nextInt();
		int B =sc.nextInt();
		int C =sc.nextInt();
		int D=A*B*C;
		int[] arr=new int[10];
		while(true) {
			for(int i=0; i<10; i++) {
				if(D%10==i) {
					arr[i]++;
					D/=10;
					break;
				}
			}
			if(D==0) {
				for(int j=0; j<10; j++) {
					System.out.println(arr[j]);
				}
				break;
			}
		}

	}

}