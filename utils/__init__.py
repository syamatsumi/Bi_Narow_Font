# utils/__init__.py


# �p�X����Ă݂āA�����Ȃ��p�X�͍폜����
# ys_closepath(glyph)
from .ys_fontforge_Remove_artifacts import ys_closepath

# �����ɑ΂��ċɒ[�ɖʐς̏����ȃR���^�[���폜����֐�
# ys_rm_spikecontours(glyph, a_thresh=0.01, p_thresh=10)
from .ys_fontforge_Remove_artifacts import ys_rm_spikecontours

# �I���J�[�u�|�C���g2�����̃G�������g�A���Ԃ�S�~�Ȃ̂ō폜����B
# rm_littleline(glyph, min_distance=20)
from .ys_fontforge_Remove_artifacts import ys_rm_little_line

# �o�E���f�B���O�{�b�N�X�Ŕ��肵�āA�������l�ȉ��̃I�u�W�F�N�g�͍폜����B
#  ys_rm_small_poly(glyph, width_threshold, height_threshold)
from .ys_fontforge_Remove_artifacts import ys_rm_small_poly



# ���Ȍ����̉����X�N���v�g�B�ɒ[�Ȋp�x���ۂ߂���ʂ����B
# �������glyph.removeOverlap()�ŏd�������_���������ƁB
# rm_self_insec(glyph, angle_threshold=2)
from .ys_fontforge_Repair_Self_Intersections import ys_repair_Self_Insec



# ���Ȍ��������X�N���v�g�Ŋp�x���L���Ď��s����B
# 1�`6�x�܂ł���Ă݂āA�_���ł�1�x�̉����͓K�p����B
# ys_Repair_Self_Intersections(glyph)
from .ys_fontforge_tryfix import ys_repair_si_chain

# �g��k���ƒP�����Ō덷����肭�܂�܂��ďC������Ȃ����Ȃ����Ċ֐��B
# ys_rescale_chain(glyph)
from .ys_fontforge_tryfix import ys_rescale_chain

# �ׂ����P�����̐ݒ���s��������
# ys_simplify(glyph)
from .ys_fontforge_tryfix import ys_simplify



# �����L���邽�߂̃X�g���[�N��ǉ�����B
# �����m���Ŏ��Ȍ����𔭐�������̂ŏ��u�K�{�B
# ys_widestroke(glyph, stroke_width, storoke_height)
from .ys_fontforge_widestroke import ys_widestroke



# �����������Ɋg��������������ƕ����������̂ŁA
# ���ƂȂ鏈�����珜�O���邽�߂̃��X�g�ƃt���O�����̂��߂ɁB
# �O���f�[�^���������������̂�������񂯂ǁB
# ys_list_invglyph(input_str, flag)
from .ys_invglyph_list import ys_list_invglyph
