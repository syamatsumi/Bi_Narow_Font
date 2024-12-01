#!fontforge --lang=py -script

import fontforge
import math

# �I���J�[�u�_�̃m�[�h����2��葽��(�܂�3�ȏ�)�̃p�X��ok_paths�ɕۑ��B
# 2�_�Ԃ̋�������萔�ȏ゠��Ȃ�A�J�}�{�R��̌`������Ă�\��������B
# �ⓚ���p�ō폜����ꍇ��min_distance���N�\�f�J�ɐݒ肷�邱�ƁB

def ys_rm_little_line(glyph, min_distance=20):
    ok_paths = []  # �L���ȃp�X��ۑ����郊�X�g
    for contour in glyph.foreground:
        # �I���N���[�u�|�C���g�𒊏o
        on_curve_points = [point for point in contour if point.on_curve]
        
        # �I���N���[�u�|�C���g��2�_�̏ꍇ�ɋ������v�Z
        if len(on_curve_points) == 2:
            distance = math.sqrt(
                (on_curve_points[0].x - on_curve_points[1].x)**2
                +(on_curve_points[0].y - on_curve_points[1].y)**2
                )
            if distance > min_distance:
                ok_paths.append(contour)  # �������������OK
        elif len(on_curve_points) > 2:
            # �I���N���[�u�|�C���g��3�_�ȏ�̏ꍇ�͖�������OK
            ok_paths.append(contour)

    # �t�H�A�O���E���h���N���A���āAOK�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ok_paths:  # OK�p�X�̏����߂�
        glyph.foreground += contour



# �o�E���f�B���O�{�b�N�X�Ŕ��肵�āA
# �������l�ȉ��̃I�u�W�F�N�g�͍폜����B

def ys_rm_small_poly(width_threshold, height_threshold, glyph):
# ����main�Ŏg���ƕ��v���p�e�B����������֐����ȊO�Ŏg������_���B
# �w�肳�ꂽ臒l��菬�������̂�NG�p�X�ϐ��ɓ����
    ng_paths = []  # �󃊃X�g��������
    for contour in glyph.foreground:  # �e�p�X�i�֊s�j�����[�v
        contour.addExtrema("all")
        bbox = contour.boundingBox()
        xmin, ymin, xmax, ymax = bbox
        width = xmax - xmin
        height = ymax - ymin
        if width <= width_threshold and height <= height_threshold:  # �������`�F�b�N
            ng_paths.append(contour)  # �����𖞂������̂����X�g�ɒǉ�
    # ���̂Ȃ��p�X(�������ۑ��ł��ĂȂ��R���^�[)��OK�ϐ��Ƀu�`����
    ok_paths = [contour for contour in glyph.foreground if contour not in ng_paths]
    # �t�H�A�O���E���h���N���A���āAOK�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ok_paths:  # ok�p�X�̏����߂�
        glyph.foreground += contour



if __name__ == "__main__":
    ys_rm_littleline(glyph, 20)