import java.util.ArrayList;
import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] Card = new int[N];
		for(int i=0; i<N; i++) {
			Card[i]=sc.nextInt();
		}
		ArrayList<Integer> list = new ArrayList<Integer>();
			
		for(int j=0; j<N; j++) {
			for( int k=0; k<j; k++) {
				for( int l=0; l<k; l++) {
					list.add(Card[j]+Card[k]+Card[l]);
										
				}
			}
			
		}
		
		int Jacpot = 0;
		for(int i=0; i<list.size(); i++) {
			
		
	
		}
		
		
		
		for(int i=0; i<list.size(); i++) {
			if(Jacpot<=list.get(i) && list.get(i)<=M) {
				Jacpot=list.get(i);
				} 
			
			
				
			}
		
		System.out.println(Jacpot);
			
	}

}