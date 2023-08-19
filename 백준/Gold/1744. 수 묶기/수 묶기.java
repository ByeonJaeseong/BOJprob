import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<Integer> pList = new ArrayList<Integer>();
		List<Integer> zList = new ArrayList<Integer>();
		List<Integer> nList = new ArrayList<Integer>();
		long sum = 0;
		for(int i=0; i<N; i++) {
			int a = Integer.parseInt(br.readLine());
			if(a==1) {
				sum=(long)sum+a;
			}else if(a>0) {
				pList.add(a);
			}else if(a==0) {
				zList.add(a);
			}else {
				nList.add(a);
			}
		}
		pList.sort(null);
		nList.sort(null);
		int p = pList.size();
		for(int i=p-1; 0<i; i=i-2) {
			sum=(long) sum + pList.get(i)*pList.get(i-1);
			//System.out.println("i:"+(pList.get(i))+" i-1:"+(pList.get(i-1))+" sum:"+sum);
			pList.remove(i);
			pList.remove(i-1);
		}
		if(pList.size()==1) {
			sum+=pList.get(0);
		}
		int q = nList.size();
		for(int i=0; i<q-1; i=i+2) {
			sum=(long) sum + nList.get(0)*nList.get(1);
			nList.remove(0);
			nList.remove(0);
		}
		
		if(nList.size()==1 && zList.size()==0) {
			sum +=nList.get(0);
		}
		
		System.out.println(sum);
	
		
		

	}

}