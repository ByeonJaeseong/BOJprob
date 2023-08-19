import java.util.TreeSet;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int N = sc.nextInt();
	    ArrayList<Integer> list = new ArrayList<Integer>(); 
	    TreeSet<Integer> ts= new TreeSet<Integer>();
		for(int i=0; i<N; i++){
		    int M =sc.nextInt();
		    list.add(M);
		}
        list.sort(Comparator.naturalOrder());
        
		for(int i=0; i<N; i++){
		    ts.add(list.get(i)*(N-i));
		}
		int max = ts.pollLast();
		System.out.println(max);
	}
}
