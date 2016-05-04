import java.util.*;
import java.io.*;

class Atom
{
	private String name;
	private String symbol;
	private int protons;
	private int neutrons;
	private double mass;//amu FTW
	private int[][] electrons;
	private double electronegativity;//Pauling Electronegativity
	
	//***************************Constructors***************************
	public Atom(int p)
	{
		protons = p;
		electrons = new int[7][];
		for(int x = 0; x < 7; x ++)
			electrons[x] = new int[x+1];
		for(int x = 0; x < electrons.length; x ++)
			for(int y = 0; y < x; y ++)
				electrons[x][y] = 0;
		fillElectrons(p);
		try
		{
			Scanner input = new Scanner(new File("Atom_data\\"+p+".txt"));
			name = input.next();
			symbol = input.next();
			neutrons = input.nextInt();
			mass = input.nextDouble();
			electronegativity = input.nextDouble();
		}
		catch(IOException e)
		{
			System.out.println(e);
			name = ""+p;
			symbol = ""+p;
			neutrons = (int)Math.round(.0051*p*p+1.1286*p-1.3944);
			mass = protons + neutrons;
//			electronegativity = getStabilityScore();
			electronegativity = 0;
		}
	}
	//***************************Mutators***************************
	public void fillElectrons(int count)
	{
		int n = 1;
		int l = 0;
		for(int s = 1; s < 9; s ++)
		{
			if(count <= 0)
				break;
			n = s/2 + 1;
			l = s - n;
			while(l > -1 && l < n)
			{
				while(count > 0 && electrons[n-1][l] < 4 * l + 2)
				{
					electrons[n-1][l] += 1;
					count --;
				}
				n ++;
				l --;
				if(count <= 0)
					break;
			}
			if(count <= 0)
				break;
		}
	}
//	public void addElectrons()
//	public void removeElectrons()
//	public void exciteElectron(int nstart, int lstart, int nend, int lend)
	//Bonds/bonding Electrons
	//bond type(Ionic, Covalent), sigma, pi, Strength
	//create bonds, bond type
	
	//***************************Accessors***************************
	public String getName()
	{
		return name;
	}
	public String getSymbol()
	{
		return symbol;
	}
	public int getProtons()
	{
		return protons;
	}
	public int getNeutrons()
	{
		return neutrons;
	}
	public double getMass()
	{
		return mass;
	}
	public int[][] getElectrons()
	{
		return electrons;
	}
	public int getNumElectrons()
	{
		int sum = 0;
		for(int[] EL:electrons)
			for(int e:EL)
				sum += e;
		return sum;
	}
	public double getElectronegativity()
	{
		return electronegativity;
	}
//	public String getElectronConfiguration()// claculated from electrons[][]
	public int getCharge()
	{
		return protons - getNumElectrons();
	}
//	public boolean getMagnetism() //False - Paramagnetic, True - Diamagnetic
//	public double getStabilityScore()//based on orbitals filled/half filled, energy levels, and neuclear charge, similar to electronegativity
	//***************************Setters***************************
	public void setName(String n)
	{
		name = n;
	}
	public void setSymbol(String s)
	{
		symbol = s;
	}
	public void setNeutrons(int n)
	{
		mass = mass - neutrons + n;
		neutrons = n;
	}
	public void setMass(double m)
	{
		if(Math.abs(m - protons - neutrons) > 1)
		{
			neutrons = neutrons  + (int)(m - mass);
		}
		mass = m;
	}
//	public void setElectrons(boolean[] e)//or maybe swap electrons, check charge is not too large
//	public void setCharge(int c)//changes number of electrons to match charge
}