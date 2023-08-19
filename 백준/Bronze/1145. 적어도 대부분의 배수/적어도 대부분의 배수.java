import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr= new int[5];
		for(int i=0; i<arr.length;i++) {
			arr[i]=sc.nextInt();
		}
		int j=1;
		while(true) {
			int a=0;		
			for(int i=0;i<arr.length;i++) {
				if(j%arr[i]==0) {
					a++;
				}
			}
			if(a>=3) {
				break;
			}else {
				j++;
			}
		}
		System.out.println(j);
		

	}
	public static int min(int[] arr) {
		int a=0;
		for(int i=0; i<arr.length-1;i++) {
			if(arr[i]<=arr[i+1]) {
				a=arr[i];
			}
			else {
				a=arr[i+1];
			}			
		}
		return a;
	}

}
