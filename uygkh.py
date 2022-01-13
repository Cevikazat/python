#include<stdio.h>
islem=()
main=()
int(main()) ;{

int(islem):
int(bakiye) = 1000;
int(tutar):


print(f"islemler\n1:para cekme\n2:para yatırma\n3:havale yapma\n4:bakiye sorgula\n5:kartı iade ediniz");

print(f"islem seciniz");
scan(f"%d",&islem);

switch(islem){

case 1:
    printf("bakiyeniz %d",bakiye);
    printf("cekilecek tutar");
    scanf("%d",&tutar);
    if (tutar > bakiye){
        printf("bakiye yetersiz\n");
    }
    bakiye -=tutar;
    printf("bakiyeniz %d",bakiye);
break;

case 2:
    printf("bakiyeniz %d",bakiye);
    printf("yatırılacak tutar");
    scanf("%d",&tutar);

    bakiye +=tutar;
    printf("bakiyeniz %d\n",bakiye);
break;

case 3:
    printf("bakiyeniz %d",bakiye);
    printf("havale yapılacak tutar");
    scanf("%d",&tutar);

    if (tutar > bakiye){
        printf("bakiye yetersiz");

        bakiye -=tutar;
        printf("bakiyeniz %d\n",bakiye);
        }
break;

case 4:
    printf("bakiyeniz %d\n",bakiye);

break;

case 5:
    printf("bakiyeniz %d",bakiye);
    printf("kartınız iade edildi\n");

break;
}






return 0;
}