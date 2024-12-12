#!fontforge --lang=py -script

import fontforge
import math

# �J�����p�X����āA�����Ȃ��p�X���̂Ă�֐�
def ys_closepath(glyph):
    # �p�X������ꂽ�R���^�[��OK�p�X�ϐ��Ƀu�`���ށA
    ok_paths = [contour.dup() for contour in glyph.foreground if contour.closed]
    # �p�X���J�����R���^�[(�������ۑ��ł��ĂȂ��R���^�[)��NG�ϐ��Ƀu�`����
    ng_paths = [contour.dup() for contour in glyph.foreground if contour not in ok_paths]
    # �t�H�A�O���E���h���N���A���āANG�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ng_paths:  # NG�p�X�̏����߂�
        glyph.foreground += contour
    # �J�����p�X����鑀��
    for contour in glyph.foreground:
        contour.addExtrema("all")
        contour.closed = True  # �����I�ɕ���

    # �����I�ɕ��邱�Ƃ��ł����p�X��OK�p�X�ϐ��Ƀu�`���ށA
    ok_paths += [contour.dup() for contour in glyph.foreground if contour.closed]
    glyph.foreground = fontforge.layer()  # �܂��c���Ă�S�~�͒��߂ă|�C�B
    for contour in ok_paths:  # OK�p�X�������߂�
        glyph.foreground += contour
    
    glyph.addExtrema("all")
    return



# �ʐς��ȈՓI�Ɍv�Z����֐�
# �����̓I���J�[�u�|�C���g�����v�����Ă����ǁA�悭�l����������Ɋւ��Ă�
# �S�Ẵ|�C���g������ߎ�������������萳�m�Ȃ̂ŕύX�B
def contour_area_and_points(contour):
    try:
        on_pts = []
        for i in range(len(contour)):
            if contour[i].type != 'offcurve':
                on_pts.append(contour[i])
        if len(on_pts) < 3:
            return 0.0, len(on_pts)
        x = [p.x for p in on_pts]
        y = [p.y for p in on_pts]
        area = 0.0
        for i in range(len(on_pts)):
            j = (i + 1) % len(on_pts)
            area += x[i]*y[j] - y[i]*x[j]
    except AttributeError as e:  # �����̖�肪����ꍇ
        print(f"AttributeError: {e}")
        return 0.0, 0
    except Exception as e:  # ����ȊO�̗\�����ʃG���[
        print(f"Unexpected error: {e}")
        return 0.0, 0
    return abs(area)*0.5, len(on_pts)

# �R���^�[�̎������ȈՓI�Ɍv�Z����֐�
def contour_length_and_points(contour):
    try:
        all_pts = []
        for i in range(len(contour)):
            all_pts.append(contour[i])
        length = 0.0
        for i in range(len(all_pts)):
            j = (i + 1) % len(all_pts)
            dx = all_pts[j].x - all_pts[i].x
            dy = all_pts[j].y - all_pts[i].y
            length += math.sqrt(dx*dx + dy*dy)
    except AttributeError as e:  # �����̖�肪����ꍇ
        print(f"AttributeError: {e}")
        return 0.0, 0
    except Exception as e:  # ����ȊO�̗\�����ʃG���[
        print(f"Unexpected error: {e}")
        return 0.0, 0
    return length, len(all_pts)

# �����ɑ΂��ċɒ[�ɖʐς̏����ȃR���^�[���폜����֐�
def ys_rm_spikecontours(glyph, c_thresh=0.1, g_thresh=0.001, p_thresh=10):
    ok_paths = []  # �L���ȃp�X��ۑ����郊�X�g
    # �O���t�S�̖̂ʐς��擾
    g_bbox = glyph.boundingBox()  # bbox: (xMin, yMin, xMax, yMax)
    gmax_area = (g_bbox[2] - g_bbox[0]) * (g_bbox[3] - g_bbox[1])

    if glyph.validate(1) & 0x01:  # �󂢂��p�X�����݂���ꍇ
        ys_closepath(glyph)  # �󂢂��p�X�������I�ɕ���֐�

    for contour in glyph.foreground:
        length, points = contour_length_and_points(contour)
        # �������Ȃ��Ȃ�ʐϔ��0�Ŋm��B
        if length == 0:
            c_ratio = 0.0
            g_ratio = 0.0

        # ����g�񂾃R���^�[�i���Ȃǁj�́A�O�����ɑ΂���ʐς�
        # �ɒ[�ɒႭ�o�邽�߁A���_���������A���R���^�[�̊O������
        # BBOX�̊O�����𒴂���ꍇ�̂݁ABBOX�̖ʐςƔ�r����B
        else:
            if points > p_thresh:  # �_�̐���������
                bbox = contour.boundingBox()
                # [xmin, ymin, xmax, ymax] ��Ԃ��z��Ōv�Z�B
                bbox_pe = 2 * ((bbox[2] - bbox[0]) + (bbox[3] - bbox[1]))

                # BBOX�̎�����蒷���Ƃ���BBOX�̖ʐς���r�Ώ�
                if length > bbox_pe:
                    cmax_area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
                else:
                    cmax_area = (length/4)**2
            else:  # ��L�̂ǂ���̏����ɂ����Ă͂܂�Ȃ��ꍇ�͊O������B
                cmax_area = (length/4)**2

            # �R���^�[�̊T�Z�ʐς����߂�cmax_area�Ɣ�r����B
            area, _ = contour_area_and_points(contour)
            c_ratio = area/cmax_area if cmax_area > 0 else 0.0
            # �S�̂ɔ䂵�Ă̖ʐϔ����r����B
            g_ratio = area/gmax_area if gmax_area > 0 else 0.0

        # �ǂ��炩�̊���ʐϔ䂪�傫�����OK
        if c_ratio > c_thresh or g_ratio > g_thresh:
            ok_paths.append(contour.dup())  # ���i�p�X�ɒǉ�

    # �t�H�A�O���E���h���N���A���āAOK�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ok_paths:  # OK�p�X�̏����߂�
        glyph.foreground += contour
    return



# �I���J�[�u�_�̃m�[�h����2��葽��(�܂�3�ȏ�)�̃p�X��ok_paths�ɕۑ��B
# 2�_�Ԃ̋�������萔�ȏ゠��Ȃ�A�J�}�{�R��̌`������Ă�\��������B
# �ⓚ���p�ō폜����ꍇ��min_distance���N�\�f�J�ɐݒ肷�邱�ƁB
# ���̂����C���֐��ɓ����ƃO���t����������A���Ԃ�Q�Ɠn���������B
# �����炭����ŉ��������n�Y�c�c
def ys_rm_isolatepath(glyph, min_distance=20):
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
                ok_paths.append(contour.dup())  # �������������OK
        elif len(on_curve_points) > 2:
            # �I���N���[�u�|�C���g��3�_�ȏ�̏ꍇ�͖�������OK
            ok_paths.append(contour)
    return



# �o�E���f�B���O�{�b�N�X�Ŕ��肵�āA
# �������l�ȉ��̃I�u�W�F�N�g�͍폜����B
def ys_rm_small_poly(glyph, width_threshold, height_threshold):
    ng_paths = []  # �󃊃X�g��������
    for contour in glyph.foreground:  # �e�p�X�i�֊s�j�����[�v
        contour.addExtrema("all")
        bbox = contour.boundingBox()
        xmin, ymin, xmax, ymax = bbox
        width = xmax - xmin
        height = ymax - ymin
        if width <= width_threshold and height <= height_threshold:  # �������`�F�b�N
            ng_paths.append(contour.dup())  # �����𖞂������̂����X�g�ɒǉ�
    # ���̂Ȃ��p�X(�������ۑ��ł��ĂȂ��R���^�[)��OK�ϐ��Ƀu�`����
    ok_paths = [contour.dup() for contour in glyph.foreground if contour not in ng_paths]
    # �t�H�A�O���E���h���N���A���āAOK�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ok_paths:  # ok�p�X�̏����߂�
        glyph.foreground += contour



if __name__ == "__main__":
    ys_rm_littleline(glyph, 20)