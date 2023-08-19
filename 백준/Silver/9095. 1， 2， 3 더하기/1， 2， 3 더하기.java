import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int T = sc.nextInt();
		int[] arr = new int[T];
		for(int i=0; i<T; i++) {
			arr[i]=sc.nextInt();
		}
		int[] arr1= new int[12];
		arr1[0]=0;
		arr1[1]=1;
		arr1[2]=2;
		arr1[3]=4;
		for(int i=4; i<=11; i++) {
			arr1[i]=arr1[i-1]+arr1[i-2]+arr1[i-3];
		}
		for(int i=0; i<T; i++) {
			System.out.println(arr1[arr[i]]);
		}

	}

}
