from threading import Lock
def init():
    global bunch_CT_patches, bunch_GTV_patches,bunch_CT_patches2, bunch_GTV_patches2,mutex,mutex2
    global bunch_CT_patches_vl, bunch_GTV_patches_vl,bunch_CT_patches_vl2, bunch_GTV_patches_vl2, patch_count
    global bunch_Penalize_patches,bunch_Penalize_patches2,bunch_Penalize_patches_vl,bunch_Penalize_patches_vl2
    global train_queue, read_patche_mutex_tr,read_patche_mutex_vl,tr_isread,vl_isread
    global queue_isready_vl, validation_totalimg_patch, validation_patch_reuse, read_vl_offline, read_off_finished
    queue_isready_vl = False



    validation_totalimg_patch = 1980
    read_vl_offline = False
    read_off_finished = False

    patch_count=0
    mutex= Lock()
    mutex2= Lock()
    read_patche_mutex_tr= Lock()
    read_patche_mutex_vl= Lock()
    train_queue=Lock()
    bunch_CT_patches=[]
    bunch_GTV_patches=[]
    bunch_Penalize_patches=[]

    tr_isread=True
    vl_isread = True
    bunch_CT_patches2=[]
    bunch_GTV_patches2=[]
    bunch_Penalize_patches2=[]

    bunch_CT_patches_vl=[]
    bunch_GTV_patches_vl=[]
    bunch_Penalize_patches_vl=[]

    bunch_CT_patches_vl2=[]
    bunch_GTV_patches_vl2=[]

    bunch_Penalize_patches_vl2 = []
    validation_patch_reuse = []