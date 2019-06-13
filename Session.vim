let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/shopMgmt/odoo
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd addons/auto_service_shop/models/vehicle.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
enew
file NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=10
setlocal nofen
tabnext 1
badd +1 .gitmodules
badd +62 addons/auto_service_shop/models/vehicle.py
badd +21 addons/auto_service_shop/security/ir.model.access.csv
badd +0 NERD_tree_2
badd +1 addons/auto_service_shop/models/service_ticket.py
badd +83 addons/auto_service_shop/models/auto_service.py
badd +3 addons/auto_service_shop/views/vehicle_action.xml
badd +5 addons/auto_service_shop/views/vehicle_template.xml
badd +7 addons/auto_service_shop/views/vehicle_views.xml
badd +33 addons/auto_service_shop/__manifest__.py
badd +4 addons/auto_service_shop/security/security.xml
badd +1 addons/auto_service_shop/5
badd +76 addons/auto_service_shop/views/auto_service_views.xml
badd +0 .mailmap
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOSc
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
