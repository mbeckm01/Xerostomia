#!/usr/bin/python3

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi']=300

df= pd.read_csv(r'/users/micaelabeckman/desktop/ParsedXeroDryIntersectionNodeTable.csv')
saliva=df[['display name','tissue::saliva']]
#ax=saliva['tissue::saliva'].plot(kind='bar',title='Saliva Expression',figsize=(15,10),legend=True)

#ax.set_ylabel('Saliva expression')
saliva.plot(x='display name', y='tissue::saliva',kind='bar',title='Saliva Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)

plt.savefig('SalivaExpressionIntersection')

heart=df[['display name','tissue::heart']]
heart.plot(x='display name', y='tissue::heart',kind='bar',title='Heart Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('HeartExpressionIntersection')

intestine=df[['display name','tissue::intestine']]
intestine.plot(x='display name', y='tissue::intestine',kind='bar',title='Intestine Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('IntestineExpressionIntersection')

kidney=df[['display name','tissue::kidney']]
kidney.plot(x='display name', y='tissue::kidney',kind='bar',title='Kidney Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('KidneyExpressionIntersection')

liver=df[['display name','tissue::liver']]
liver.plot(x='display name', y='tissue::liver',kind='bar',title='liver Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('LiverExpressionIntersection')

nervous_system=df[['display name','tissue::nervous system']]
nervous_system.plot(x='display name', y='tissue::nervous system',kind='bar',title='Nervous System Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('NervousSysExpressionIntersection')

muscle=df[['display name','tissue::muscle']]
muscle.plot(x='display name', y='tissue::muscle',kind='bar',title='Muscle Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('MuscleExpressionIntersection')

lung=df[['display name','tissue::lung']]
lung.plot(x='display name', y='tissue::lung',kind='bar',title='Lung Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('LungExpressionIntersection')

spleen=df[['display name','tissue::spleen']]
spleen.plot(x='display name', y='tissue::spleen',kind='bar',title='spleen Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('spleenExpressionIntersection')

'''lymph_node=df[['display name','tissue::lymph node']]
lymph_node.plot(x='display name', y='tissue::lymph node',kind='bar',title='Lymph Node Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('LymphNodeExpressionIntersection')'''

pancreas=df[['display name','tissue::pancreas']]
pancreas.plot(x='display name', y='tissue::pancreas',kind='bar',title='Pancreas Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('PancreasExpressionIntersection')

skin=df[['display name','tissue::skin']]
skin.plot(x='display name', y='tissue::skin',kind='bar',title='Skin Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('skinExpressionIntersection')

stomach=df[['display name','tissue::stomach']]
stomach.plot(x='display name', y='tissue::stomach',kind='bar',title='Stomach Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('StomachExpressionIntersection')

'''thyroid_gland=df[['display name','tissue::thyroid gland']]
thyroid_gland.plot(x='display name', y='tissue::thyroid_gland',kind='bar',title='Thyroid Gland Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('TyhroidGlandExpressionIntersection')'''

bone=df[['display name','tissue::bone marrow']]
bone.plot(x='display name', y='tissue::bone marrow',kind='bar',title='Bone Marrow Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('BoneExpressionIntersection')

adrenal=df[['display name','tissue::adrenal gland']]
adrenal.plot(x='display name', y='tissue::adrenal gland',kind='bar',title='Adrenal Gland Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('AdrenalExpressionIntersection')

urine=df[['display name','tissue::urine']]
urine.plot(x='display name', y='tissue::urine',kind='bar',title='Urine Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('UrineExpressionIntersection')

blood=df[['display name','tissue::blood']]
blood.plot(x='display name', y='tissue::blood',kind='bar',title='Blood Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('BloodExpressionIntersection')

eye=df[['display name','tissue::eye']]
eye.plot(x='display name', y='tissue::eye',kind='bar',title='Eye Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('EyeExpressionIntersection')

gallbladder=df[['display name','tissue::gall bladder']]
gallbladder.plot(x='display name', y='tissue::gall bladder',kind='bar',title='Gall Bladder Expression',fontsize=6)
plt.xlabel('Gene name',fontsize=2)
plt.savefig('GallBladderExpressionIntersection')