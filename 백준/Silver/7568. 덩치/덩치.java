import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] arr = new int[N][3];
		for(int i=0; i<N; i++) {
			for(int j=0; j<2; j++) {
				arr[i][j]=sc.nextInt();
			}
		}
		
		for(int i=0; i<N; i++) {
			int a=1;
			for(int j=0; j<N; j++) {
			
				if((arr[i][0]<arr[j][0])&&(arr[i][1]<arr[j][1])) {
					a++;
				}
			}
			if(i!=N-1) {
			System.out.print(a+" ");
			}else {
			System.out.print(a);
			}
			a=1;
		}


	}

}