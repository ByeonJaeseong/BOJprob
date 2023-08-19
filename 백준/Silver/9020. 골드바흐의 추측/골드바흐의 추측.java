import java.util.LinkedList;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		LinkedList<Integer> list = new LinkedList();
		LinkedList<Integer> list2 = new LinkedList();
		TreeSet<Integer> ts= new TreeSet<Integer>();
		TreeSet<Integer> ts2= new TreeSet<Integer>();
		for(int i=1; i<9999; i++) {
			ts.add(i+1);
		}
		Integer a=ts.first();
		
		while(true) {
			int b=2;
			while(a*b<10000) {
				ts.remove((Integer)a*b);
				b++;
			}
			a=ts.higher(a);
			if(a==null) {
				break;
			}
		}
		
	
		
		int n =sc.nextInt();
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			arr[i]=sc.nextInt();
		}
		
		for(int i=0; i<n; i++) {
			int p = arr[i];
			int q = p/2;
			while(true) {
			
				if(ts.contains(q)) {
					if(ts.contains(p-q)) {
						System.out.print(q);
						System.out.print(" ");
						System.out.print(p-q);
						System.out.println();
						break;
					}else {
						q=ts.lower(q);
					}
				}else {
					q=ts.lower(q);
				}
				
			}
		}

	}

}
