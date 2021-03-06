#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import datetime
import argparse
from global_dict.w_global import gbl_set_value, gbl_get_value, gbl_save_value
from model.w_train import train_a_unet


def usage():
    print("Error in input argv")


def main():
    parser = argparse.ArgumentParser(
        description='''This is a beta script for sCT generation from PET/MR images. ''',
        epilog="""All's well that ends well.""")
    parser.add_argument('--slice_x', metavar='', type=int, default=1,
                        help='Slices of input(1)<int>[1/3]')
    parser.add_argument('--color_mode', metavar='', type=int, default=1,
                        help='Slices of input(1)<int>[1/3]')

    parser.add_argument('--size_x', metavar='', type=int, default=64,
                        help='chunk size: x dimension')
    parser.add_argument('--size_y', metavar='', type=int, default=64,
                        help='chunk size: y dimension')
    parser.add_argument('--size_z', metavar='', type=int, default=32,
                        help='chunk size: z dimension')

    parser.add_argument('--stride_x', metavar='', type=int, default=8,
                        help='stride of the x dimension')
    parser.add_argument('--stride_y', metavar='', type=int, default=8,
                        help='stride of the x dimension')
    parser.add_argument('--stride_z', metavar='', type=int, default=8,
                        help='stride of the x dimension')

    parser.add_argument('--id', metavar='', type=str, default="chansey",
                        help='ID of the current model.(eeVee)<str>')
    parser.add_argument('--epoch', metavar='', type=int, default=400,
                        help='Number of epoches of training(300)<int>')
    parser.add_argument('--n_filter', metavar='', type=int, default=32,
                        help='The initial filter number(64)<int>')
    parser.add_argument('--depth', metavar='', type=int, default=4,
                        help='The depth of U-Net(4)<int>')
    parser.add_argument('--batch_size', metavar='', type=int, default=8,
                        help='The batch_size of training(10)<int>')
    parser.add_argument('--content_weight', metavar='', type=int, default=2500e9,
                        help='The content weight of perceptual loss<int>')
    parser.add_argument('--style_weight', metavar='', type=int, default=11000e9,
                        help='The style weight of perceptual loss<int>')

    parser.add_argument('--train_path', metavar='', type=str, default='./data/train',
                        help='The path of training dataset <str>')
    parser.add_argument('--val_path', metavar='', type=str, default='./data/val',
                        help='The path of validation dataset<str>')
    parser.add_argument('--pretrained_path', metavar='', type=str, default='',
                        help='The pretrained path of model<str>')
    parser.add_argument('--vgg_path', metavar='', type=str,
                        default='',
                        help='The path of vgg model<str>')

    args = parser.parse_args()

    dir_syn = './result/' + str(args.size_x) + '-' + str(args.size_y) + '-' + str(args.size_z) + '/'
    dir_model = './result/' + str(args.size_x) + '-' + str(args.size_y) + '-' + str(args.size_z) + '/'

    if not os.path.exists(dir_syn):
        os.makedirs(dir_syn)

    if not os.path.exists(dir_model):
        os.makedirs(dir_model)

    time_stamp = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M")
    model_id = args.id + time_stamp
    gbl_set_value("depth", args.depth)
    gbl_set_value("dir_syn", dir_syn)
    gbl_set_value("dir_model", dir_model)
    gbl_set_value("model_id", model_id)
    gbl_set_value("n_epoch", args.epoch + 1)
    gbl_set_value("n_filter", args.n_filter)
    gbl_set_value("depth", args.depth)
    gbl_set_value("batch_size", args.batch_size)
    gbl_set_value("color_mode", args.color_mode)
    gbl_set_value("slice_x", args.slice_x)
    gbl_set_value("size_x", args.size_x)
    gbl_set_value("size_y", args.size_y)
    gbl_set_value("size_z", args.size_z)
    gbl_set_value("stride_x", args.stride_x)
    gbl_set_value("stride_y", args.stride_y)
    gbl_set_value("stride_z", args.stride_z)
    gbl_set_value("content_weight", args.content_weight)
    gbl_set_value("style_weight", args.style_weight)
    gbl_set_value("pretrained_path", args.pretrained_path)
    gbl_set_value("vgg_path", args.vgg_path)
    gbl_set_value("train_path", args.train_path)
    gbl_set_value("val_path", args.val_path)

    model = train_a_unet(pretrained_model=0)
    print("Training Completed!")


if __name__ == "__main__":
    main()
